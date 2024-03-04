struct User {
    name: String,
    email: String,
}

impl User {
    fn new(name: &str) -> User {
        User {
            name: name.to_string(),
            email: format!("{}@arjancodes.com", name),
        }
    }
}

fn get_user_option(name: &str) -> Option<User> {
    if name == "Arjan" {
        Some(User::new(name))
    } else {
        None
    }
}

fn get_user_result(name: &str) -> Result<User, String> {
    if name == "Arjan" {
        Ok(User::new(name))
    } else {
        Err(String::from("User not found"))
    }
}

fn main() {
    // by default variables are not mutable, but you can make them using 'mut'
    // ex let mut user = User::new("Arjan");
    let user = User::new("Arjan");
    println!("Hello, {}!", user.name);
    println!("Your email is: {}", user.email);

    let user_option = get_user_option("Arjan");
    match user_option {
        Some(user) => println!("User option: {:?}", user.name),
        None => println!("User not found"),
    }
}
