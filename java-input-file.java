import java.util.*;

// Interface for printable objects
interface Printable {
    void printDetails();
}

// Base class for all entities in the library
abstract class Entity implements Printable {
    private String id;
    private String name;

    public Entity(String id, String name) {
        this.id = id;
        this.name = name;
    }

    // Getters and Setters
    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public void printDetails() {
        System.out.println("ID: " + id + ", Name: " + name);
    }
}

// Author class
class Author extends Entity {
    private String biography;

    public Author(String id, String name, String biography) {
        super(id, name);
        this.biography = biography;
    }

    public String getBiography() {
        return biography;
    }

    @Override
    public void printDetails() {
        super.printDetails();
        System.out.println("Biography: " + biography);
    }
}

// Book class
class Book extends Entity {
    private Author author;
    private String genre;
    private boolean isAvailable;

    public Book(String id, String name, Author author, String genre) {
        super(id, name);
        this.author = author;
        this.genre = genre;
        this.isAvailable = true;
    }

    public Author getAuthor() {
        return author;
    }

    public String getGenre() {
        return genre;
    }

    public boolean isAvailable() {
        return isAvailable;
    }

    public void setAvailable(boolean available) {
        isAvailable = available;
    }

    @Override
    public void printDetails() {
        super.printDetails();
        System.out.println("Author: " + author.getName());
        System.out.println("Genre: " + genre);
        System.out.println("Availability: " + (isAvailable ? "Available" : "Not Available"));
    }
}

// LibraryMember class
class LibraryMember extends Entity {
    private List<Book> borrowedBooks;

    public LibraryMember(String id, String name) {
        super(id, name);
        this.borrowedBooks = new ArrayList<>();
    }

    public void borrowBook(Book book) throws Exception {
        if (!book.isAvailable()) {
            throw new Exception("Book is not available for borrowing.");
        }
        book.setAvailable(false);
        borrowedBooks.add(book);
        System.out.println("Book '" + book.getName() + "' borrowed by " + getName());
    }

    public void returnBook(Book book) {
        if (borrowedBooks.remove(book)) {
            book.setAvailable(true);
            System.out.println("Book '" + book.getName() + "' returned by " + getName());
        } else {
            System.out.println("Book '" + book.getName() + "' was not borrowed by " + getName());
        }
    }

    @Override
    public void printDetails() {
        super.printDetails();
        System.out.println("Borrowed Books:");
        for (Book book : borrowedBooks) {
            book.printDetails();
        }
    }
}

// Library class (Composition)
class Library {
    private List<Book> books;
    private List<LibraryMember> members;

    public Library() {
        this.books = new ArrayList<>();
        this.members = new ArrayList<>();
    }

    public void addBook(Book book) {
        books.add(book);
    }

    public void addMember(LibraryMember member) {
        members.add(member);
    }

    public void displayBooks() {
        System.out.println("Library Books:");
        for (Book book : books) {
            book.printDetails();
        }
    }

    public void displayMembers() {
        System.out.println("Library Members:");
        for (LibraryMember member : members) {
            member.printDetails();
        }
    }
}

// Main class
public class LibraryManagementSystem {
    public static void main(String[] args) {
        // Create authors
        Author author1 = new Author("A1", "J.K. Rowling", "British author best known for the Harry Potter series.");
        Author author2 = new Author("A2", "George Orwell", "English novelist known for '1984' and 'Animal Farm'.");

        // Create books
        Book book1 = new Book("B1", "Harry Potter and the Philosopher's Stone", author1, "Fantasy");
        Book book2 = new Book("B2", "1984", author2, "Dystopian");

        // Create library members
        LibraryMember member1 = new LibraryMember("M1", "Alice");
        LibraryMember member2 = new LibraryMember("M2", "Bob");

        // Create library and add books and members
        Library library = new Library();
        library.addBook(book1);
        library.addBook(book2);
        library.addMember(member1);
        library.addMember(member2);

        // Display library details
        library.displayBooks();
        library.displayMembers();

        // Borrow and return books
        try {
            member1.borrowBook(book1);
            member2.borrowBook(book2);
            member1.returnBook(book1);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }

        // Display updated library details
        library.displayBooks();
        library.displayMembers();
    }
}
