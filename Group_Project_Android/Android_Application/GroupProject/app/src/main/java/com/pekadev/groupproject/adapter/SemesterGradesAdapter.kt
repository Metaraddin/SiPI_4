package com.pekadev.groupproject.adapter

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.pekadev.groupproject.R
import com.pekadev.modelview.LoadInfoMethods
import com.pekadev.modelview.Student
import kotlinx.android.synthetic.main.viewpager_item.view.*
import kotlinx.coroutines.MainScope
import kotlinx.coroutines.launch

class SemesterGradesAdapter(var student: Student) : RecyclerView.Adapter<SemesterGradesAdapter.PagerVH>() {
    init{
        LoadInfoMethods.loadMarks(student, ::notifyInMainThread)
    }
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): PagerVH =
        PagerVH(LayoutInflater.from(parent.context).inflate(R.layout.viewpager_item, parent, false))

    fun notifyInMainThread(){
        MainScope().launch{
            notifyDataSetChanged()
        }
    }
    override fun getItemCount(): Int {
        return student.recordBook.semestersCount()
    }

    override fun onBindViewHolder(holder: PagerVH, position: Int){
        holder.itemView.semNumberView.text = holder.itemView.resources.getString(R.string.semester)+(position+1)
        holder.itemView.examsTextView.text = student.recordBook.getExamsInSem((position+1).toString())
        holder.itemView.testsTextView.text = student.recordBook.getTestInSem((position+1).toString())
    }

    class PagerVH(itemView: View) : RecyclerView.ViewHolder(itemView)
}

