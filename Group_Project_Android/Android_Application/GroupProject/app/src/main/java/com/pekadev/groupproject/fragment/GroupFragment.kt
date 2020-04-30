package com.pekadev.groupproject.fragment

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.EdgeEffect
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.DividerItemDecoration
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.pekadev.groupproject.R
import com.pekadev.groupproject.adapter.GroupAdapter
import com.pekadev.groupproject.adapter.MainActivityAdapter
import kotlinx.android.synthetic.main.group_fragment.*


class GroupFragment : Fragment(), MainActivityFragment {

    companion object {
        fun newInstance() = GroupFragment()
    }


    private var adapter = GroupAdapter()
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return inflater.inflate(R.layout.group_fragment, container, false)
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        groupsRecycler.adapter = adapter
        groupsRecycler.layoutManager = LinearLayoutManager(this.context)
        groupsRecycler.addItemDecoration(
            DividerItemDecoration(
                groupsRecycler.context,
                DividerItemDecoration.VERTICAL
            )
        )
        groupsRecycler.edgeEffectFactory = object : RecyclerView.EdgeEffectFactory() {
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
