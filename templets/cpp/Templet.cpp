#include "Templet.hpp"

// Constructors
Templet::Templet(void)
{
	std::cout << "\e[0;33mDefault Constructor called of Templet\e[0m" << std::endl;
}

Templet::Templet(const Templet &copy)
{
	*this = copy;
	std::cout << "\e[0;33mCopy Constructor called of Templet\e[0m" << std::endl;
}


// Destructor
Templet::~Templet()
{
	std::cout << "\e[0;31mDestructor called of Cat\e[0m" << std::endl;
}


// Operators
Templet & Templet::operator=(const Templet &assign)
{
	this->_type = assign.getType();
	std::cout << "\e[0;31mDestructor called of Templet\e[0m" << std::endl;
	return (*this);
}

// Getters / Setters
std::string Cat::getType() const
{
	return (_type);
}


// Member functions

