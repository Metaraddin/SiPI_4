package com.pekadev.modelview

import com.pekadev.model.Methods
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.invoke
import kotlinx.coroutines.launch
import java.lang.Exception

object AuthorizationActivityMethods {
    fun login(id:String, password:String, callback: ()->Unit){
        try{
            GlobalScope.launch {
                //var result = Methods.authorization(id, password)
//            if ((result as ArrayList<*>).isEmpty()){
//                return@launch
//            }
                EmployeeAccount.setData()
                (Dispatchers.Main){
                    callback.invoke()
                }
            }
        }
        catch (e: Exception){
            e.printStackTrace()
        }


    }
}