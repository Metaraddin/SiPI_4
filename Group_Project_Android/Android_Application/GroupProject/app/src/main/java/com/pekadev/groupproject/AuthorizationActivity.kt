package com.pekadev.groupproject

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.pekadev.modelview.AuthorizationActivityMethods
import kotlinx.android.synthetic.main.activity_authorization.*


class AuthorizationActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_authorization)
        ViewListenersMethods.setEditTextFocusListener(idEditText, textView)
        ViewListenersMethods.setEditTextFocusListener(passwordEditText, textView2)
        login_button.setOnClickListener{
            AuthorizationActivityMethods.login(passwordEditText.text.toString(), idEditText.text.toString()) {
                switchToMainApplication()
            }
        }
    }

     private fun switchToMainApplication(){
         var intent =  Intent(applicationContext, MainActivity::class.java);
         intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
         startActivity(intent)
         finish()
    }




}
