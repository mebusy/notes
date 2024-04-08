

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


