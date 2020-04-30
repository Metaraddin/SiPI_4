package com.pekadev.modelview

import com.pekadev.model.Config
import java.util.regex.Pattern

object Settings {
    private const val zeroTo255 = "([01]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])"
    private const val IP_REGEXP = (zeroTo255 + "\\." + zeroTo255 + "\\."
            + zeroTo255 + "\\." + zeroTo255)
    private val IP_PATTERN: Pattern = Pattern.compile(IP_REGEXP)
    fun setIp(ip: String) : Boolean{
        var result = IP_PATTERN.matcher(ip).matches()
        if (result){
            Config.IP = ip
        }
        return result

    }
    fun getIp():String{
        return Config.IP
    }
    fun setPort(port: String) : Boolean{
        if (port.toInt()<=65535){
            Config.PORT = port.toInt()
            return true
        }
        return false

    }
    fun getPort():String{
        return Config.PORT.toString()
    }

}