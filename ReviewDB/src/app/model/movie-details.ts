// MovieDetails is a data object that describes one movie.
export interface MovieDetails {
  movieTitle: string;
  movieYear: number;
  movieSummary: string;
  movieDirector: string;
  forChildren: boolean;
  actorList: Actor[];
}

// Actor is a data object that describes one actor.
export interface Actor {
    name: string;
}