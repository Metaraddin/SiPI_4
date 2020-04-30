package com.pekadev.groupproject.fragment


import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.EdgeEffect
import androidx.recyclerview.widget.DividerItemDecoration
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.pekadev.groupproject.R
import com.pekadev.groupproject.adapter.MainActivityAdapter
import com.pekadev.groupproject.adapter.StudentAdapter
import com.pekadev.modelview.Group
import kotlinx.android.synthetic.main.group_fragment.*
import kotlinx.android.synthetic.main.students_fragment.*


class StudentsFragment : Fragment(), MainActivityFragment {

    companion object {
        fun newInstance() = StudentsFragment()
    }

    var adapter = StudentAdapter()
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.students_fragment, container, false)
    }

    fun setAdapterWithGroup(group: Group){
        adapter = StudentAdapter(group)
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        studentsRecycler.adapter = adapter
        studentsRecycler.layoutManager = LinearLayoutManager(this.context)
        studentsRecycler.addItemDecoration(
            DividerItemDecoration(
                studentsRecycler.context,
                DividerItemDecoration.VERTICAL
            )
        )
        studentsRecycler.edgeEffectFactory = object : RecyclerView.EdgeEffectFactory() {
            override fun createEdgeEffect(view: RecyclerView, direction: Int): EdgeEffect {
                return EdgeEffect(view.context).apply { color = resources.getColor(android.R.color.darker_gray) }
            }
        }
    }

    override fun getAdapter(): MainActivityAdapter {
        return adapter
    }

    override fun prefersChanged() {
        adapter.filter("")
    }

}
