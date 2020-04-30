package com.pekadev.groupproject

import android.content.Intent
import android.os.Bundle
import android.view.MenuItem
import androidx.appcompat.app.AppCompatActivity
import com.pekadev.modelview.Settings
import kotlinx.android.synthetic.main.activity_settings.*


class SettingsActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_settings)
        title = "Настройки"
        val actionBar: android.app.ActionBar? = actionBar
        actionBar?.setDisplayHomeAsUpEnabled(true)
        ViewListenersMethods.setPortEditTextFocusListener(portTextEdit, portTextView)
        ViewListenersMethods.setIpEditTextFocusListener(ipTextEdit, ipTextView)
        portTextEdit.setText(Settings.getPort())
        ipTextEdit.setText(Settings.getIp())
    }
    override fun onOptionsItemSelected(item: MenuItem?): Boolean {
        val myIntent = Intent(applicationContext, MainActivity::class.java)
        startActivityForResult(myIntent, 0)
        return true
    }

    override fun onDestroy() {
        Settings.setPort(portTextEdit.text.toString())
        Settings.setIp(ipTextEdit.text.toString())
        super.onDestroy()
    }
}
