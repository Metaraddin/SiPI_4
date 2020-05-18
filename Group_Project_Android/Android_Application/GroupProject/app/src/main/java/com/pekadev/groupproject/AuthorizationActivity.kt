package com.pekadev.groupproject

import android.content.Context
import android.content.Intent
import android.content.SharedPreferences
import android.graphics.PorterDuff
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.pekadev.modelview.AuthorizationActivityMethods
import kotlinx.android.synthetic.main.activity_authorization.*


class AuthorizationActivity : AppCompatActivity() {
    lateinit var sPref: SharedPreferences
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        autoLogin()
        setContentView(R.layout.activity_authorization)
        ViewListenersMethods.setEditTextFocusListener(idEditText, textView)
        ViewListenersMethods.setEditTextFocusListener(passwordEditText, textView2)
        login_button.setOnClickListener{
            AuthorizationActivityMethods.login(idEditText.text.toString(),passwordEditText.text.toString(), ::switchToMainApplication, ::highlightText)
        }
        imageButton.setOnClickListener{
            var intent =  Intent(applicationContext, SettingsActivity::class.java)
            startActivity(intent)
        }
    }

    override fun onPause() {
        if (checkBox.isChecked){
            saveData()
        }

        super.onPause()
    }

    fun saveData(){
        sPref = getSharedPreferences("auth", Context.MODE_PRIVATE)
        var ed = sPref.edit()
        ed.putString("login", idEditText.text.toString())
        ed.putString("password", passwordEditText.text.toString())
        ed.apply()

    }

    fun autoLogin(){
        sPref = getSharedPreferences("auth", Context.MODE_PRIVATE)
        if (sPref.contains("login")){
            AuthorizationActivityMethods.login(sPref.getString("login", " ")!!,sPref.getString("password", " ")!!, ::switchToMainApplication, ::highlightText)
        }
    }

     private fun switchToMainApplication(){
         var intent =  Intent(applicationContext, MainActivity::class.java);
         intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP)
         startActivity(intent)
         finish()
    }

    private fun highlightText(){
        var unFocusErrorColor = resources.getColor(android.R.color.holo_red_dark)
        idEditText.background.setColorFilter(unFocusErrorColor, PorterDuff.Mode.SRC_IN)
        passwordEditText.background.setColorFilter(unFocusErrorColor, PorterDuff.Mode.SRC_IN)
        Toast.makeText(this, "Данные введены некорректно!", Toast.LENGTH_LONG).show()
    }




}
