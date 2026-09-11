**`Eq`, `PartialEq` and `Hash` basics**

| Trait | Purpose | Typical use |
|-------|---------|-------------|
| `PartialEq` | Defines equality (`==`, `!=`). | Most structs & enums derive it automatically. |
| `Eq` | Indicates that equality is an *equivalence relation* (reflexive, symmetric, transitive). Must be implemented if the type can be used in hashed collections (e.g., `HashSet`, `HashMap` keys). | Usually derived together with `PartialEq`. |
| `Hash` | Gives a hash value used by `HashSet`/`HashMap`. | Derivable for most types; implement manually if hashing must ignore some fields or use custom hashing logic. |

---

### Deriving automatically

```rust
use std::collections::{HashSet, HashMap};

#[derive(Debug, PartialEq, Eq, Hash)]
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    // Using a HashSet
    let mut points = HashSet::new();
    points.insert(Point { x: 1, y: 2 });

    // Using a HashMap
    let mut scores: HashMap<Point, u32> = HashMap::new();
    scores.insert(Point { x: 1, y: 2 }, 10);
}
```

`derive` expands to implementations that compare **all fields** and hash all fields in the order they appear. This is suitable when all fields are relevant for identity.

---

### Manual implementation

If you need custom equality or hashing (e.g., ignore a field, normalize values), implement `PartialEq`, `Eq`, and `Hash` yourself:

```rust
use std::hash::{Hash, Hasher};

struct User {
    id: u64,
    nickname: String,
    // other fields that shouldn't affect hashing/equality
    last_login: std::time::SystemTime,
}

impl PartialEq for User {
    fn eq(&self, other: &Self) -> bool {
        self.id == other.id
    }
}
impl Eq for User {}

impl Hash for User {
    fn hash<H: Hasher>(&self, state: &mut H) {
        self.id.hash(state);
    }
}
```

Only `id` participates in equality and hashing; `nickname` and `last_login` are ignored. This lets `User` be stored in `HashSet`/`HashMap` keyed by `id`.

---

### Common pitfalls

| Issue | Fix |
|-------|-----|
| Forgetting `Eq` when deriving `Hash` | Derive `Eq` or implement it manually. |
| Hashing floating‑point values (`f32`, `f64`) | Use `ordered_float` crate or convert to a canonical form (e.g., `to_bits()`). |
| Hash collisions | If hash quality matters, switch to `FxHashMap` or a custom hasher, but most cases default `SipHasher` is sufficient. |
| Mutating a key while in a hash collection | Never modify fields that influence equality/hash while the key is in a `HashMap`/`HashSet`. If needed, remove and re‑insert. |

---

### Quick checklist for using `HashSet`/`HashMap`

1. **Define the key type**
   - Derive `PartialEq + Eq + Hash` if all fields matter, else implement manually.
2. **Insert**
   - `hash_set.insert(value);`
   - `hash_map.insert(key, value);`
3. **Lookup**
   - `hash_set.contains(&query);`
   - `hash_map.get(&key);`
4. **Iteration**
   - `for v in &hash_set { … }`
   - `for (k, v) in &hash_map { … }`

---

**Resources**

- [Rust docs – `HashSet`](https://doc.rust-lang.org/std/collections/struct.HashSet.html)
- [Rust docs – `HashMap`](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Rust Book – Custom Types](https://doc.rust-lang.org/book/ch10-02-traits.html)
- [Crate: `ordered-float`](https://crates.io/crates/ordered-float) for hashing floats safely.
