package com.pekadev.modelview

import com.pekadev.model.Methods
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch

object Filter {
    var hashMap: Map<String, ArrayList<String>> = HashMap()
    var preferredFaculty: String? = null
    var preferredSpeciality: String? = null
    init{
        loadMap()
    }
    fun loadMap(){
        GlobalScope.launch {
            hashMap = Methods.loadUniqueFacultyMap()
        }
    }
    fun getUniqueFaculty():ArrayList<String>{
        if (hashMap.isEmpty()){
            loadMap()
        }
        return ArrayList(hashMap.keys)
    }


}