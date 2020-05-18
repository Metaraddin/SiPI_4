package com.pekadev.model

object Methods {
    fun authorization(id: String, password: String) : Any{
        var connection = Connection()
        connection.execute("Select * from employee where login='$id' and password = '$password';")
        return connection.result
    }

    fun loadGroups():Any{
        var connection = Connection()
        connection.execute("select * from groups;")
        return connection.result
    }


    fun loadUniqueFacultyMap():HashMap<String, ArrayList<String>> {
        var connection = Connection()
        connection.execute("select faculty, specialty from groups group by faculty, specialty;")
        var facultyMap = HashMap<String, ArrayList<String>>()
        for (i in connection.result as ArrayList<ArrayList<String>>){
            if (!facultyMap.containsKey(i[0])){
                facultyMap[i[0]] = ArrayList()
            }
            facultyMap[i[0]]!!.add(i[1])
        }
        return facultyMap
    }

    fun loadStudents(groupId: String = "group_id") : Any{
        var connection = Connection()
        connection.execute("select * from student join groups on student.group_id = groups.id where group_id = $groupId;")
        return connection.result

    }

    fun loadStudentExams(studentId: String):Any{
        var connection = Connection()
        connection.execute("select discipline_id, name, mark, semester from statement_exam join discipline on statement_exam.discipline_id = discipline.id where statement_exam.student_id = $studentId;")
        return connection.result
    }

    fun loadStudentTests(studentId: String):Any{
        var connection = Connection()
        connection.execute("select discipline_id, name, mark, semester from statement_test join discipline on  statement_test.discipline_id = discipline.id where statement_test.student_id = $studentId;")
        return connection.result
    }


    fun loadStudent(studentId: String):Any{
        var connection = Connection()
        connection.execute("select * from student join groups on student.group_id = groups.id where student.id = $studentId;")
        return connection.result
    }

}