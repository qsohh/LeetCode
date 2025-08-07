# print function

```cpp
template<typename... Args>
void print(Args&&... args) {((std::cout << args << ", "), ...) << '\n';}
```

