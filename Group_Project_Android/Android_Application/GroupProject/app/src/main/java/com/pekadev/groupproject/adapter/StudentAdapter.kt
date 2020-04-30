package com.pekadev.groupproject.adapter

import android.content.Intent
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
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

class StudentAdapter(group: Group? = null) : RecyclerView.Adapter<StudentAdapter.StudentViewHolder>(), MainActivityAdapter {
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

    fun notifyInMainThread(){
        MainScope().launch{
            filter("")
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): StudentViewHolder {
        val value = LayoutInflater.from(parent.context)
            .inflate(R.layout.student_list_item, parent, false)
        return StudentAdapter.StudentViewHolder(value)
    }

    override fun getItemCount(): Int {
        return arrCopy.size
    }

    override fun onBindViewHolder(holder: StudentViewHolder, position: Int) {
        holder.itemView.studentIdView.text = holder.itemView.resources.getString(R.string.book)+arrCopy[position].id
        holder.itemView.studentFullNameView.text = arrCopy[position].fullName
        holder.itemView.studentGroupIdView.text = holder.itemView.resources.getString(R.string.group)+arrCopy[position].groupId
        holder.itemView.setOnClickListener {
            val intent = Intent(holder.itemView.context, StudentActivity::class.java)
            intent.putExtra("student", arrCopy[position])
            ContextCompat.startActivity(holder.itemView.context, intent, null)
        }
    }

    override fun filter(exp: String) {
        arrCopy = ArrayList<Student>()
        for (i in original){
            if (i.fullName.contains(exp) and i.getFaculty().contains(Filter.preferredFaculty ?: "") and i.getSpecialty().contains(Filter.preferredSpeciality ?: "")){
                arrCopy.add(i)
            }
        }
        notifyDataSetChanged()
    }


}