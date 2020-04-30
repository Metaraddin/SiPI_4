package com.pekadev.groupproject

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.pekadev.groupproject.fragment.GroupFragment
import com.pekadev.groupproject.fragment.StudentsFragment
import com.pekadev.modelview.Group
import kotlinx.android.synthetic.main.activity_group.*


class GroupActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_group)
        val intent = intent
        var group = intent.getSerializableExtra("group") as Group
        title = resources.getString(R.string.group)+group.id
        var frag = StudentsFragment()
        frag.setAdapterWithGroup(group)
        supportFragmentManager.beginTransaction().replace(R.id.frameLayout2, frag).commit()
    }
}
