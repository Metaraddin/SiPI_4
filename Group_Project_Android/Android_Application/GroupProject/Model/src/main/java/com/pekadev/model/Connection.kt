package com.pekadev.model
import java.io.DataOutputStream
import java.io.ObjectInputStream
import java.lang.Exception
import java.net.Socket


class Connection {
    lateinit var result: Any
    fun execute(order: String){
        try {
            var socket = Socket(Config.IP, Config.PORT)
            val oos = DataOutputStream(socket.getOutputStream())
            val ois = ObjectInputStream(socket.getInputStream())
            oos.writeUTF(order)
            while (!::result.isInitialized){
                result = ois.readObject()
            }
            ois.close()
            oos.flush()
        }
        catch (e: Exception){
            if (!::result.isInitialized){
                result = ArrayList<Array<String>>()
            }
            return
        }

    }
}