#ifndef FOX_HPP
#define FOX_HPP

class Fox {
 public:
  // Constructor
  Fox(void);
  Fox(const Fox& obj);
  // Destructor
  ~Fox(void);
  // Operators
  Fox &operator=(const Fox &assign)
};

#endif // FOX_HPP
