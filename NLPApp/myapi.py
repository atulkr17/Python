

// Import
import paralleldots.Komprehend

// Setting your API key
// Get your API key here
Komprehend pd = new Komprehend("<YOUR_API_KEY>");

// Examples
String sentiment = pd.sentiment('Come on, lets play together');
Console.WriteLine(sentiment);