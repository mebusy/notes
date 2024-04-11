

slice reference
     let a = [1, 2, 3, 4, 5];
     let nice_slice = &a[1..4];

解构
     let cat = ("Furry McFurson", 3.5);
     let (name, age) = cat;

tuple
     let numbers = (1, 2, 3);
     let second = numbers.1;

struct clone
   #[derive(Debug, Clone)]
     ...
     let mut your_order = order_template.clone();

vec 1
    let a = [10, 20, 30, 40]; // a plain array
    let v = vec![10, 20, 30, 40]; // a vector

vec 2
     fn vec_loop(mut v: Vec<i32>) -> Vec<i32> {
         for element in v.iter_mut() {
             *element = *element * 2;
         }
     }

    fn vec_map(v: &Vec<i32>) -> Vec<i32> {
        v.iter()
            .map(|element| {
                element * 2
            }).collect()
    }



mod 1

```rust
mod delicious_snacks {
    // You can bring module paths into scopes and provide new names for them with
    // the 'use' and 'as' keywords. Fix these 'use' statements to make the code
    pub use self::fruits::PEAR as fruit;
    pub use self::veggies::CUCUMBER as veggie;
```

especially from the Rust standard library into your scope

```rust
use std::time::{SystemTime, UNIX_EPOCH};
```


hashmap

```rust
        // get existing team or create a new one
        // update the goals scored and conceded
        // insert the team back into the hashmap
        let team_1 = scores.entry(team_1_name).or_insert(Team {
            goals_scored: 0,
            goals_conceded: 0,
        });
        team_1.goals_scored += team_1_score;
```


parent scope

```rust
    super::xxx
```

Option

- Option<T>
    - Some(T) / None
    - normally use `if let` or `while let` to filter out the None value

Result

- Result<T,E>
    - Ok(T) / Err(E)


