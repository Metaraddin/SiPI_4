package com.pekadev.groupproject.fragment

import androidx.recyclerview.widget.RecyclerView
import com.pekadev.groupproject.adapter.MainActivityAdapter

interface MainActivityFragment {

    fun getAdapter():MainActivityAdapter

    fun prefersChanged()

}