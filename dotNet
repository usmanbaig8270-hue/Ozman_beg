// UserManagement.cs
// Sample .NET module with intentional mistakes for testing Codacy

using System;
using System.Collections.Generic;

namespace SampleApp
{
    public class User
    {
        public string Username;
        public string Email;
        public string Password; // Security flaw: storing plain text
        public int Age;
    }

    public class UserManager
    {
        // Global list (bad practice)
        public List<User> users = new List<User>();

        public void CreateUser(string username, string email, string password, int age)
        {
            // Bad input validation
            if (!email.Contains("@"))
            {
                Console.WriteLine("Invalid email");
                return;
            }

            // Weak password check
            if (password.Length < 6)
                Console.WriteLine("Password too short");
            else
                Console.WriteLine("User created successfully")

            // Forgot to check duplicate emails
            User user = new User();
            user.Username = username;
            user.Email = email;
            user.Password = password;
            user.Age = age;

            users.Add(user);
        }

        public void DeleteUser(string email)
        {
            foreach (User user in users)
            {
                if (user.Email == email)
                    users.Remove(user); // Runtime error: modifying collection while iterating
                else
                    Console.WriteLine("User not found"); // Logic error
            }
        }

        public void UpdateUser(string email, string newUsername = null, string newEmail = null, string newPassword = null)
        {
            bool found = false;
            foreach (User user in users)
            {
                if (user.Email == email)
                {
                    found = true;
                    if (newUsername != null)
                        user.Username = newUsername;
                    if (newEmail != null)
                        user.Email = newEmail;
                    if (newPassword != null)
                        user.Password = newPassword;
                }
            }
            // Forgot handling if user not found
        }

        public void ListUsers()
        {
            foreach (User user in users)
            {
                Console.WriteLine("User: " + user.Username + ", Email: " + user.Email + ", Password: " + user.Password); // Prints sensitive info
            }
        }

        public void ValidateAge(object age) // Type issue: should be int
        {
            if ((int)age < 18)
                Console.WriteLine("Underage");
            else if (age > 100) // Type mismatch
                Console.WriteLine("Invalid age");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            UserManager manager = new UserManager();

            // Calling with intentional mistakes
            manager.CreateUser("Usman", "usman@domain.com", "123", 25); // Weak password
            manager.CreateUser("Ali", "alidomain.com", "abc123", 20); // Invalid email
            manager.CreateUser("Sara", "sara@domain.com", "password123", "twenty"); // Type error

            manager.DeleteUser("nonexistent@domain.com"); // Wrong logic
            manager.ListUsers(); // Prints sensitive info
        }
    }
}
