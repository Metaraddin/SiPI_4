package com.pekadev.modelview

import com.pekadev.model.Methods
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch
import javax.security.sasl.AuthorizeCallback

object LoadInfoMethods {

    fun loadGroupStudents(group: Group, dataChangeCallback: ()->Unit){
        GlobalScope.launch {
            group.addStudents(Methods.loadStudents(group.id) as ArrayList<ArrayList<String>>)
            dataChangeCallback.invoke()
        }

    }

    fun loadAllStudents(students: ArrayList<Student>, dataChangeCallback: ()->Unit){
        students.clear()
        GlobalScope.launch {
            var data = Methods.loadStudents() as ArrayList<ArrayList<String>>
            for (i in data){
                students.add(Student(i))
            }
            dataChangeCallback.invoke()
        }

    }
    fun loadGroups(groups: ArrayList<Group>, dataChangeCallback: ()->Unit){
        groups.clear()
        GlobalScope.launch {
            var data = Methods.loadGroups() as ArrayList<ArrayList<String>>
            for (i in data){
                groups.add(Group(i))

            }
            dataChangeCallback.invoke()

        }
    }
    fun loadMarks(student: Student, dataChangeCallback: ()->Unit){
        GlobalScope.launch {
            student.recordBook.addExams(Methods.loadStudentExams(student.id) as ArrayList<ArrayList<String>>)
            student.recordBook.addTests(Methods.loadStudentTests(student.id) as ArrayList<ArrayList<String>>)
            dataChangeCallback.invoke()
        }
    }
}