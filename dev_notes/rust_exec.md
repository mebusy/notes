

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


Box<dyn ???>

any type which implements a particular trait ??? ,  think as interface in other languages.


`impl<T> Wrapper<T> ...`


Lifetime

`fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {`


collect()方法可以被用来将一个可迭代对象转成任意类型的集合，包括数组、向量、链表、哈希表等等

    words
        .iter()
        .map(|word| capitalize_first(word))
        .collect::<Vec<String>>()  // 如果编译器不能推断类型，则需要指定 collect的类型
        .join("")


`Box` - a smart pointer used to store data on the heap, which also allows us  to wrap a recursive type.

pub enum List {
    Cons(i32, Box<List>),
    Nil,
}


## multiple owners via the Rc<T> type


```rust
let sun = Rc::new(Sun {});
let mercury = Planet::Mercury(Rc::clone(&sun)); // sun.clone() is not recommended

drop(mercury);
```



## Arc (Atomically Reference Counted)

```rust
let numbers: Vec<_> = (0..100u32).collect();
let shared_numbers = Arc::new(numbers);

let child_numbers = Arc::clone(&shared_numbers);
```


## share a struct between threads

```rust
use std::sync::{Arc, Mutex};
use std::thread;
use std::time::Duration;

struct JobStatus {
    jobs_completed: u32,
}

fn main() {
    let status = Arc::new(Mutex::new(JobStatus { jobs_completed: 0 }));
    let mut handles = vec![];
    for _ in 0..10 {
        let status_shared = Arc::clone(&status);
        let handle = thread::spawn(move || {
            thread::sleep(Duration::from_millis(250));
            // TODO: You must take an action before you update a shared value to make it safe to share between threads
            let mut status_shared = status_shared.lock().unwrap();
            status_shared.jobs_completed += 1;

        });
        handles.push(handle);
    }
    for handle in handles {
        handle.join().unwrap();
        // TODO: Print the value of the JobStatus.jobs_completed. Did you notice
        // anything interesting in the output? Do you have to 'join' on all the
        // handles?
        println!("jobs completed {}", status.lock().unwrap().jobs_completed);
    }
}
```

## as 

Type casting in Rust is done via the usage of the `as` operator. Please note that the `as` operator is not only used when type casting. It also helps with renaming imports.

```rust
    total / values.len() as f64
```





