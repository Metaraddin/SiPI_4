package com.pekadev.groupproject


import android.content.Intent
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.view.View
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.widget.SearchView
import com.pekadev.groupproject.fragment.FilterFragment
import com.pekadev.groupproject.fragment.GroupFragment
import com.pekadev.groupproject.fragment.MainActivityFragment
import com.pekadev.groupproject.fragment.StudentsFragment
import com.pekadev.modelview.Filter
import kotlinx.android.synthetic.main.activity_main.*


class MainActivity : AppCompatActivity() {
    lateinit var currentFragment : MainActivityFragment
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setSupportActionBar(bottom_app_bar)
        currentFragment = GroupFragment()
        title = "Список групп"
        supportFragmentManager.beginTransaction().replace(R.id.frameLayout,
            currentFragment as GroupFragment
        ).commit()
        Filter
        fab.setOnClickListener {
            Filter.loadMap()
            FilterFragment().show(
                supportFragmentManager,
                "Filter"
            ) }

    }
    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        val inflater = menuInflater
        inflater.inflate(R.menu.main_menu, menu)
        var searchItem = menu?.findItem(R.id.app_bar_search)
        searchItem!!.setOnActionExpandListener(OnActionExp(menu!!))
        var searchView = searchItem!!.actionView as SearchView
        searchView.setOnQueryTextListener(object :
            SearchView.OnQueryTextListener {
            override fun onQueryTextSubmit(query: String): Boolean {
                return try{
                    currentFragment.getAdapter().filter(query)
                    true
                } catch (ex : Exception){
                    false
                }
            }

            override fun onQueryTextChange(newText: String): Boolean {
                return try{
                    currentFragment.getAdapter().filter(newText)
                    true
                } catch (ex : Exception){
                    false
                }

            }
        })
        return true
    }
    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        when (item.itemId) {
            R.id.app_bar_settings -> {
                var intent =  Intent(applicationContext, SettingsActivity::class.java)
                startActivity(intent)
            }
            R.id.app_bar_group ->{
                currentFragment = GroupFragment()
                title = "Список групп"
                supportFragmentManager.beginTransaction().replace(R.id.frameLayout,
                    currentFragment as GroupFragment
                ).commit()
            }
            R.id.app_bar_student ->{
                currentFragment = StudentsFragment()
                title = "Список студентов"
                supportFragmentManager.beginTransaction().replace(R.id.frameLayout,
                    currentFragment as StudentsFragment
                ).commit()
            }
        }

        return super.onOptionsItemSelected(item)

    }

    inner class OnActionExp(private val menu:Menu) : MenuItem.OnActionExpandListener{

        override fun onMenuItemActionExpand(item: MenuItem?): Boolean {
            menu.findItem(R.id.app_bar_group).isVisible = false
            menu.findItem(R.id.app_bar_student).isVisible = false
            menu.findItem(R.id.app_bar_settings).isVisible = false
            this@MainActivity.fab.visibility = View.GONE
            return true
        }

        override fun onMenuItemActionCollapse(item: MenuItem?): Boolean {
            menu.findItem(R.id.app_bar_group).isVisible = true
            menu.findItem(R.id.app_bar_student).isVisible = true
            menu.findItem(R.id.app_bar_settings).isVisible = true
            this@MainActivity.fab.visibility = View.VISIBLE
            return true
        }

    }
}


