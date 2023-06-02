#ifndef DOG_HPP
#define DOG_HPP

class Dog {
 public:
  // Constructor
  Dog(void);
  Dog(const Dog& obj);
  // Destructor
  ~Dog(void);
  // Operators
  Dog &operator=(const Dog &assign)
};

#endif // DOG_HPP
