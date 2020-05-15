package com.pekadev.modelview

import java.io.Serializable
import kotlin.math.max

data class Student(var params:ArrayList<String>) : Serializable{
    lateinit var group: Group
    var id = params[0]
    var groupId = params[1]
    var fullName = params[2]
    var budgetaryBasis = params[3]
    private var innerFaculty = params[5]
    private var innerSpecialty  = params[6]
    var recordBook = RecordBook()


    fun setStudentGroup(group: Group){
        this.group = group
    }

    fun setData(new_params:ArrayList<String>){
        this.params = new_params
         id = params[0]
         groupId = params[1]
         fullName = params[2]
         budgetaryBasis = params[3]
         var innerFaculty = params[5]
         var innerSpecialty  = params[6]
         var recordBook = RecordBook()
    }



    fun getFaculty() : String{
        return innerFaculty
    }
    fun getSpecialty() : String{
        return innerSpecialty
    }

    class RecordBook():Serializable{
        var exams =  ArrayList<GradeExam>()
        var tests =  ArrayList<GradeTest>()

        fun getTestInSem(sem: String):String{
            var formatted = ""
            for (i in tests){
                if (i.semester ==sem){
                    formatted+=i.getFormattedData()+"\n"
                }
            }
            return formatted
        }

        fun getExamsInSem(sem: String):String{
            var formatted = ""
            for (i in exams){
                if (i.semester ==sem){
                    formatted+=i.getFormattedData()+"\n"
                }
            }
            return formatted
        }

        fun semestersCount():Int{
            var maxint = 0
            for (i in exams){
                maxint = if (i.semester.toInt()>maxint) i.semester.toInt() else maxint
            }
            return maxint
        }

        fun addExams(args: ArrayList<ArrayList<String>>){
            for(i in args){
                exams.add(GradeExam(i))
            }
        }
        fun addTests(args: ArrayList<ArrayList<String>>){
            for(i in args){
                tests.add(GradeTest(i))
            }
        }


        abstract class Grade(args: ArrayList<String>):Serializable{
            var disciplineId : String = args[0]
            var disciplineName : String = args[1]
            var mark : String? = args[2]
            var semester: String = args[3]
            abstract fun getFormattedData():String
        }

        class GradeExam(args: ArrayList<String>) : Grade(args){

            override fun getFormattedData():String {
                return disciplineName+": "+ if (mark==null) "Не зачтено" else mark
            }

        }
        class GradeTest(args: ArrayList<String>) : Grade(args){
            override fun getFormattedData():String{
                return disciplineName+": "+ if (mark=="t") "Зачет" else "Не зачтено"
            }

        }
    }


}