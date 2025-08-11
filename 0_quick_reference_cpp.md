# print function

```cpp
template<typename... Args>
void print(Args&&... args) {((std::cout << args << ", "), ...) << '\n';}
```

# Fermat's little thm related

As $a^{p-1} \equiv 1 \pmod{p}$ (attention to the hyps), it can be induced that $a^{p-2} \equiv a^{-1} \pmod{p}$.

```cpp
using u64 = std::uint64_t;

template<typename T1, typename T2, typename T3 = u64>
u64 multimod(T1 a, T2 b, T3 mod = 1000000007) {
    u64 A = static_cast<u64>(a) % static_cast<u64>(mod);
    u64 B = static_cast<u64>(b) % static_cast<u64>(mod);
    return (A * B) % static_cast<u64>(mod);
}

template<typename T1, typename T2, typename T3 = u64>
u64 powmod(T1 a, T2 p, T3 mod = 1000000007) {
    u64 res = 1;
    u64 base = static_cast<u64>(a) % mod;
    u64 exp = static_cast<u64>(p);
    while (exp > 0) {
        if (exp & 1) { res = multimod(res, base, mod); }
        base = multimod(base, base, mod);
        exp >>= 1;
    }
    return res;
}

// InverseMod and FactorialMod to be completed
```