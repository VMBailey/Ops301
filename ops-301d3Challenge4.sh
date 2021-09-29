#!/bin/bash

menu=("Say Hello!" "Go Ping Yourself!" "Where am I?" "Exit")

echo "Welcome to what's probably the best menu you'll ever see in your entire life."
sleep 1.8

echo "Bold? Yes."
sleep 1.8

echo "True? Probably not."
sleep 1.8

echo "Select an Option:"
select choice in "${menu[@]}"
do
    case $choice in
        "Say Hello!")
            echo "Hello World!"
            ;;
        "Go Ping Yourself!")
            ping -c 4 # insert ip address here #
            ;;
        "Where am I?")
            ip a
            ;;
        "Exit")
            echo "See you, Space Cowboy"
            sleep 1.8
            break
            ;;
    esac
done
