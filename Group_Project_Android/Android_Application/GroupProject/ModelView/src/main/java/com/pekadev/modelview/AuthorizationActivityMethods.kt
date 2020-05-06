package com.pekadev.modelview

import com.pekadev.model.Methods
import kotlinx.coroutines.*
import java.lang.Exception

object AuthorizationActivityMethods {
    @ExperimentalCoroutinesApi
    fun login(id:String, password:String, onSuccessCallback: ()->Unit, onFailedCallback: ()->Unit){
        try{
            GlobalScope.launch {
                var result = Methods.authorization(id, password)
                if ((result as ArrayList<*>).isEmpty()){
                    (Dispatchers.Main){
                        onFailedCallback.invoke()
                    }
                    return@launch
                }
                EmployeeAccount.setData()
                (Dispatchers.Main){
                    onSuccessCallback.invoke()
                }
            }
        }
        catch (e: Exception){
            e.printStackTrace()
        }


    }
}