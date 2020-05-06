package com.pekadev.groupproject

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.EdgeEffect
import androidx.recyclerview.widget.RecyclerView
import com.pekadev.groupproject.adapter.SemesterGradesAdapter
import com.pekadev.modelview.Student
import kotlinx.android.synthetic.main.activity_student.*

class StudentActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_student)
        title = "Профиль студента"
        var student = intent.getSerializableExtra("student") as Student
        viewPager.adapter = SemesterGradesAdapter(student)
        nameTextView.text = student.fullName
        groupTextView.text = resources.getString(R.string.group)+student.groupId
        studentPageFacView.text = student.getFaculty()
        studentPageSpecView.text = resources.getString(R.string.speciality)+student.getSpecialty()
        (viewPager!!.getChildAt(0) as RecyclerView).edgeEffectFactory = object : RecyclerView.EdgeEffectFactory() {
            override fun createEdgeEffect(view: RecyclerView, direction: Int): EdgeEffect {
                return EdgeEffect(view.context).apply { color = resources.getColor(android.R.color.darker_gray) }
            }
        }

    }
}
