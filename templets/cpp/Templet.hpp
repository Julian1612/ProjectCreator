#ifndef TEMPLET_HPP
# define TEMPLET_HPP

class Templet
{
	public:
		// Constructors
		Templet();
		Templet(const Templet &copy);

		// Destructor
		~Templet();

		// Operators
		Templet & operator=(const Templet &assign);

		// Getters / Setters
		std::string getType() const;

		// Member functions

	private:

	protected:
};

#endif
