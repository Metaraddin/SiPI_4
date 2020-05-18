package com.pekadev.modelview

import java.io.Serializable

class Group(params:ArrayList<String>) : Serializable {
    var id = params[0]
    var facultyName = params[1]
    var speciality = params[2]
    var receiptYear = params[3]
    var callbackUpdate = { Unit}
    var students = ArrayList<Student>()



    fun addStudents(st:ArrayList<ArrayList<String>>){
        for (i in st){
            var student = Student(i)
            student.setStudentGroup(this)
            students.add(student)
        }
    }

}