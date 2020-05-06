package com.pekadev.groupproject.adapter

import android.app.Application
import android.content.Context
import android.content.Intent
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.core.content.ContextCompat
import androidx.recyclerview.widget.RecyclerView
import com.pekadev.groupproject.GroupActivity
import com.pekadev.groupproject.R
import com.pekadev.groupproject.StudentActivity
import com.pekadev.modelview.Filter
import com.pekadev.modelview.Group
import com.pekadev.modelview.LoadInfoMethods
import com.pekadev.modelview.Student
import kotlinx.android.synthetic.main.student_list_item.view.*
import kotlinx.coroutines.MainScope
import kotlinx.coroutines.launch
import java.io.Serializable

class StudentAdapter(val group: Group? = null) : RecyclerView.Adapter<StudentAdapter.StudentViewHolder>(), MainActivityAdapter, Serializable {
    var original = ArrayList<Student>()
    var arrCopy = original
    init {
        if (group==null){
            LoadInfoMethods.loadAllStudents(original, ::notifyInMainThread)

        }
        else{
            original = group.students
            LoadInfoMethods.loadGroupStudents(group, ::notifyInMainThread)
        }
    }
    class StudentViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView){
        init {
        }
    }
    fun notifyInMainThreadAtPos(pos: Int){
        MainScope().launch{
            notifyItemRemoved(pos)
        }
    }
    fun notifyInMainThread(){
        MainScope().launch{
            filter("")
            if (lastStudent!=null){
                openStudent()
            }

        }
    }

    fun openStudent(){
        for (i in arrCopy){
            if (i.id == (lastStudent?.id ?: -1)){
                val intent = Intent(context, StudentActivity::class.java)
                intent.putExtra("student", i)
                ContextCompat.startActivity(context!!, intent, null)
                return
            }
        }
        Toast.makeText(context, "Данные были изменены!", Toast.LENGTH_LONG).show()

    }


    var context: Context? = null
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): StudentViewHolder {
        val value = LayoutInflater.from(parent.context)
            .inflate(R.layout.student_list_item, parent, false)
        this.context = parent.context
        return StudentAdapter.StudentViewHolder(value)
    }

    override fun getItemCount(): Int {
        return arrCopy.size
    }
    var lastStudent: Student? = null
    override fun onBindViewHolder(holder: StudentViewHolder, position: Int) {
        holder.itemView.studentIdView.text = holder.itemView.resources.getString(R.string.book)+arrCopy[position].id
        holder.itemView.studentFullNameView.text = arrCopy[position].fullName
        holder.itemView.studentGroupIdView.text = holder.itemView.resources.getString(R.string.group)+arrCopy[position].groupId
        holder.itemView.setOnClickListener {
            lastStudent = arrCopy[position]
            if (group != null){
                LoadInfoMethods.loadGroupStudents(group, ::notifyInMainThread)
            }
            else{
                LoadInfoMethods.loadAllStudents(original, ::notifyInMainThread)
            }
//            val intent = Intent(holder.itemView.context, StudentActivity::class.java)
//            intent.putExtra("student", arrCopy[position])
//            ContextCompat.startActivity(holder.itemView.context, intent, null)
        }
    }

    override fun filter(exp: String) {
        arrCopy = ArrayList<Student>()
        for (i in original){
            if (i.fullName.toLowerCase().contains(exp.toLowerCase()) and i.getFaculty().contains(Filter.preferredFaculty ?: "") and i.getSpecialty().contains(Filter.preferredSpeciality ?: "")){
                arrCopy.add(i)
            }
        }
        notifyDataSetChanged()
    }


}