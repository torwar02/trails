const express = require("express");
const router = express.Router();

// mongodb user model
const User = require("../models/User");

// password handler
const bcrypt = require("bcrypt");

// signup
router.post("/signup", (req, res) => {
  let { firstname, lastname, email, password } = req.body;
  lastname = lastname === "" ? lastname : lastname.trim();
  firstname = firstname === "" ? firstname : firstname.trim();
  email = email === "" ? email : email.trim();
  password = password === "" ? password : password.trim();

  if (firstname == "" || lastname == "" || email == "" || password == "") {
    res.json({
      status: "FAILED",
      message: "Empty input fields!",
    });
  } else if (!/^[a-zA-Z ]*$/.test(firstname)) {
    res.json({
      status: "FAILED",
      message: "Invalid frist name entered",
    });
  } else if (!/^[a-zA-Z ]*$/.test(lastname)) {
    res.json({
      status: "FAILED",
      message: "Invalid last name entered",
    });
  } else if (!/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/.test(email)) {
    res.json({
      status: "FAILED",
      message: "Invalid email entered",
    });
  } else if (password.length < 8) {
    res.json({
      status: "FAILED",
      message: "Password is too short!",
    });
  } else {
    // checking if user already existed
    User.find({ email })
      .then((result) => {
        if (result.length) {
          res.json({
            status: "FAILED",
            message: "User with the provided email already exists",
          });
        } else {
          // password handling
          const saltRounds = 10;
          bcrypt
            .hash(password, saltRounds)
            .then((hashedPassword) => {
              const newUser = new User({
                firstname,
                lastname,
                email,
                password: hashedPassword,
              });
              newUser
                .save()
                .then((result) => {
                  res.json({
                    status: "SUCCESS",
                    message: "Signup successful",
                    data: result,
                  });
                })
                .catch(() => {
                  res.json({
                    status: "FAILED",
                    message: "An error occured while saving account",
                  });
                });
            })
            .catch(() => {
              res.json({
                status: "FAILED",
                message: "An error occured while hashing password",
              });
            });
        }
      })
      .catch((err) => {
        console.log(err);
        res.json({
          status: "FAILED",
          message: "An error occurred while checking for existing user!",
        });
      });
  }
});

// login
router.post("/login", (req, res) => {
  let { email, password } = req.body;
  email = email.trim();
  password = password.trim();
  if (email == "" || password == "") {
    res.json({
      status: "FAILED",
      message: "Empty credentials supplied",
    });
  } else {
    User.find({ email })
      .then((data) => {
        if (data) {
          // user exists
          const hashedPassword = data[0].password;
          bcrypt
            .compare(password, hashedPassword)
            .then((result) => {
              if (result) {
                res.json({
                  status: "SUCCESS",
                  message: "Signin successful",
                  data: data,
                });
              } else {
                res.json({
                  status: "FAILED",
                  message: "Invalid password entered",
                });
              }
            })
            .catch(() => {
              res.json({
                status: "FAILED",
                message: "An error occured while comparing passwords",
              });
            });
        } else {
          res.json({
            status: "FAILED",
            message: "Invalid credentials entered!",
          });
        }
      })
      .catch(() => {
        res.json({
          status: "FAILED",
          message: "An error occured while checking for existing user",
        });
      });
  }
});

module.exports = router;
