package com.pekadev.groupproject.fragment

import android.os.Bundle
import android.text.Layout
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.AdapterView
import android.widget.ArrayAdapter
import androidx.fragment.app.DialogFragment
import com.pekadev.groupproject.MainActivity
import com.pekadev.groupproject.R
import com.pekadev.modelview.Filter
import kotlinx.android.synthetic.main.filter_fragment.*

class FilterFragment : DialogFragment() {
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.filter_fragment, container, false)
    }


    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        loadData()
        facultiesSpinner.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onNothingSelected(parent: AdapterView<*>?) {

            }

            override fun onItemSelected(
                parent: AdapterView<*>?,
                view: View?,
                position: Int,
                id: Long
            ) {
                var value = parent!!.getItemAtPosition(position).toString()
                if (value!=Filter.preferredFaculty){
                    Filter.preferredSpeciality=null
                }
                var array = (if (value=="Нет") ArrayList<String>() else Filter.hashMap[value])!!
                array.add(0, "Нет")
                val prefSpec = if (Filter.preferredSpeciality == null) "Нет" else Filter.preferredSpeciality
                specialtySpinner.adapter = ArrayAdapter(this@FilterFragment.requireContext(), R.layout.spinner_item, array!!)
                specialtySpinner.setSelection( array.indexOf(prefSpec))
            }
        }
    }

    fun loadData(){
        var facult = Filter.getUniqueFaculty()
        facult.add(0, "Нет")
        facultiesSpinner.adapter = ArrayAdapter<String>(this.requireContext(), R.layout.spinner_item, facult)
        val prefFac = if (Filter.preferredFaculty == null) "Нет" else Filter.preferredFaculty
        facultiesSpinner.setSelection(facult.indexOf(prefFac))

        var specArray = ArrayList<String>()

        if (prefFac!="Нет"){
            specArray = Filter.hashMap[prefFac]!!.clone() as ArrayList<String>
        }
        specArray.add(0, "Нет")
        val prefSpec = if (Filter.preferredSpeciality == null) "Нет" else Filter.preferredSpeciality
        specialtySpinner.adapter = ArrayAdapter(this.requireContext(), R.layout.spinner_item, specArray)
        specialtySpinner.setSelection( specArray.indexOf(prefSpec))
    }

    override fun onPause() {
        saveData()
        (activity  as MainActivity).currentFragment.prefersChanged()
        super.onPause()
    }

    fun saveData(){
        Filter.preferredFaculty = if (facultiesSpinner.selectedItem.toString() == "Нет") null else facultiesSpinner.selectedItem.toString()
        Filter.preferredSpeciality = if (specialtySpinner.selectedItem.toString() == "Нет") null else specialtySpinner.selectedItem.toString()

    }
}