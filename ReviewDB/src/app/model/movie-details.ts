// MovieDetails is a data object that describes one movie.
export interface MovieDetails {
  budget: number;
  director: string;
  forAdults: boolean;
  genre: string[];
  overview: string;
  posterPath: string;
  releaseDate: string;
  releaseYear: string;
  reviews: string[];
  runtime: number;
  score: number;
  tagline: string;
  title: string;
  voteAverage: number;
  voteCount: number;
}

// Actor is a data object that describes one actor.
export interface Actor {
  name: string;
}