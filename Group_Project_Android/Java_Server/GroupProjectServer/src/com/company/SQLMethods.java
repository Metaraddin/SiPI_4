package com.company;

import java.lang.reflect.InvocationTargetException;
import java.sql.*;
import java.util.ArrayList;

public class SQLMethods {
    static Statement statement;
    public SQLMethods(){
        Connection connection = null;
        try {
            Class.forName("org.postgresql.Driver").getDeclaredConstructor().newInstance();
            connection = DriverManager
                    .getConnection(ConnectionParams.URL, ConnectionParams.USER, ConnectionParams.PASSWORD);
            statement =  connection.createStatement();
        } catch (SQLException | ClassNotFoundException | NoSuchMethodException | InstantiationException | IllegalAccessException | InvocationTargetException e) {
            e.printStackTrace();
        }
    }

    public Object executeRequest(String request){
        ArrayList<ArrayList<String>> value  = new ArrayList<>();
        synchronized (statement){
            try {
                ResultSet rs = statement.executeQuery(request);
                ResultSetMetaData rsmd = rs.getMetaData();
                int columnsNumber = rsmd.getColumnCount();

                while (rs.next()) {
                    ArrayList<String> row = new ArrayList<>();
                    for (int i = 0; i < columnsNumber; i++) {
                        row.add(rs.getString(i+1));
                    }
                    value.add(row);
                }


            } catch (SQLException e) {
                e.printStackTrace();
                System.out.println(request);
            }
            return value;
        }


    }
}
