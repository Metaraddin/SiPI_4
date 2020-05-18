package com.pekadev.groupproject.adapter

import android.content.Intent
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.core.content.ContextCompat.startActivity
import androidx.recyclerview.widget.RecyclerView
import com.pekadev.groupproject.GroupActivity
import com.pekadev.groupproject.R
import com.pekadev.modelview.Filter
import com.pekadev.modelview.Group
import com.pekadev.modelview.LoadInfoMethods
import kotlinx.android.synthetic.main.group_list_item.view.*
import kotlinx.coroutines.MainScope
import kotlinx.coroutines.launch


class GroupAdapter : RecyclerView.Adapter<GroupAdapter.GroupViewHolder>(), MainActivityAdapter {
    var original = ArrayList<Group>()
    var arrCopy = original
    init {
        LoadInfoMethods.loadGroups(original, ::notifyInMainThread)
    }
    class GroupViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView){
        lateinit var group: Group
    }

    override fun filter(exp:String){
        arrCopy = ArrayList<Group>()
        for (i in original){
            if (i.id.contains(exp) and i.facultyName.contains(Filter.preferredFaculty ?: "") and i.speciality.contains(
                    Filter.preferredSpeciality ?: "")){
                arrCopy.add(i)
            }
        }
        notifyDataSetChanged()
    }
    fun notifyInMainThread(){
        MainScope().launch{
            filter("")
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): GroupViewHolder {
        val value = LayoutInflater.from(parent.context)
            .inflate(R.layout.group_list_item, parent, false)
        return GroupViewHolder(value)
    }

    override fun getItemCount(): Int {
        return arrCopy.size
    }

    override fun onBindViewHolder(holder: GroupViewHolder, position: Int) {
        holder.itemView.groupFacultyView.text = arrCopy[position].facultyName
        holder.itemView.groupIdView.text = holder.itemView.resources.getString(R.string.group)+arrCopy[position].id
        holder.itemView.groupSpecialityView.text = holder.itemView.resources.getString(R.string.speciality)+arrCopy[position].speciality
        holder.itemView.groupYearView.text = holder.itemView.resources.getString(R.string.year)+arrCopy[position].receiptYear
        holder.itemView.setOnClickListener {
            val intent = Intent(holder.itemView.context, GroupActivity::class.java)
            intent.putExtra("group", arrCopy[position])
            startActivity(holder.itemView.context, intent, null)
        }
    }


}