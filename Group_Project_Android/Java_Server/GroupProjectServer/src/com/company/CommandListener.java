package com.company;

import org.postgresql.util.PSQLException;

import java.io.*;
import java.net.Socket;

public class CommandListener implements Runnable {

    private static Socket clientDialog;
    private static SQLMethods methods = new SQLMethods();
    public CommandListener(Socket client) {

        CommandListener.clientDialog = client;
    }
    @Override
    public synchronized void run() {
        {

            try {
                ObjectOutputStream out = new ObjectOutputStream(clientDialog.getOutputStream());
                DataInputStream in = new DataInputStream(clientDialog.getInputStream());
                while (!clientDialog.isClosed()) {
                    String str = in.readUTF();
                    out.writeObject(methods.executeRequest(str));
                    out.flush();

                }
                in.close();
                out.close();
                clientDialog.close();
            } catch (EOFException e) {
                System.out.println("OK!");
            } catch (IOException e) {
                e.printStackTrace();
            }

        }

    }

}