package com.pekadev.groupproject

import android.R
import android.graphics.PorterDuff
import android.view.View
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import com.pekadev.modelview.Settings

object ViewListenersMethods {
     fun setEditTextFocusListener(editText: EditText, textView: TextView){

        editText.onFocusChangeListener = View.OnFocusChangeListener { view, hasFocus ->
            if (hasFocus) {
                var focusColor = editText.resources.getColor(R.color.black)
                textView.setTextColor(focusColor)
                editText.background.setColorFilter(focusColor, PorterDuff.Mode.SRC_IN);
            } else {
                var unFocusColor = editText.resources.getColor(R.color.tertiary_text_dark)
                textView.setTextColor(unFocusColor)
                editText.background.setColorFilter(unFocusColor, PorterDuff.Mode.SRC_IN);

            }
        }

    }

     fun setIpEditTextFocusListener(editText: EditText, textView: TextView){

        editText.onFocusChangeListener = View.OnFocusChangeListener { view, hasFocus ->
            if (hasFocus) {
                var focusColor = editText.resources.getColor(R.color.black)
                textView.setTextColor(focusColor)
                editText.background.setColorFilter(focusColor, PorterDuff.Mode.SRC_IN)
            } else {
                var unFocusGrayColor = editText.resources.getColor(R.color.tertiary_text_dark)
                var unFocusErrorColor = editText.resources.getColor(android.R.color.holo_red_dark)

                if (!Settings.setIp(editText.text.toString())){
                    Toast.makeText(editText.context, "IP Введен некорректно!", Toast.LENGTH_LONG).show()
                    textView.setTextColor(unFocusErrorColor)
                    editText.background.setColorFilter(unFocusErrorColor, PorterDuff.Mode.SRC_IN)
                }
                else{
                    textView.setTextColor(unFocusGrayColor)
                    editText.background.setColorFilter(unFocusGrayColor, PorterDuff.Mode.SRC_IN)
                }
                editText.setText(Settings.getIp())

            }
        }

    }

    fun setPortEditTextFocusListener(editText: EditText, textView: TextView){

        editText.onFocusChangeListener = View.OnFocusChangeListener { view, hasFocus ->
            if (hasFocus) {
                var focusColor = editText.resources.getColor(R.color.black)
                textView.setTextColor(focusColor)
                editText.background.setColorFilter(focusColor, PorterDuff.Mode.SRC_IN)
            } else {
                var unFocusGrayColor = editText.resources.getColor(R.color.tertiary_text_dark)
                var unFocusErrorColor = editText.resources.getColor(android.R.color.holo_red_dark)

                if (!Settings.setPort(editText.text.toString())){
                    Toast.makeText(editText.context, "Порт введен некорректно!", Toast.LENGTH_LONG).show()
                    textView.setTextColor(unFocusErrorColor)
                    editText.background.setColorFilter(unFocusErrorColor, PorterDuff.Mode.SRC_IN)
                }
                else{
                    textView.setTextColor(unFocusGrayColor)
                    editText.background.setColorFilter(unFocusGrayColor, PorterDuff.Mode.SRC_IN)
                }
                editText.setText(Settings.getPort())

            }
        }

    }

}