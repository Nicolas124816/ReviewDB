import { Component, OnInit, ViewChild } from '@angular/core';
import { MovieService } from '../../../service/movie.service';
import { MovieDetails } from '../../../model/movie-details';
import { mockMovieList } from '../../../mock/movieListOutput';
import { FormBuilder, FormControl, FormGroup, Validators  } from '@angular/forms';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  
  movieList: MovieDetails[] = [];
  homeForm: FormGroup = new FormGroup({
    description: new FormControl(''),
    isKidsMovie: new FormControl(false),
    filterGenre: new FormControl('')
  });
  selectedMovie: any;
  isPopupVisible: boolean = false;

  constructor(private movieService: MovieService, private fb: FormBuilder) {}

  ngOnInit() {
    this.initializeForm();
  }

  initializeForm() {
    this.homeForm = this.fb.group({
      description: ['', Validators.required],
      isKidsMovie: [false],
      filterGenre: ['']
    });
  }

  getMovieList() {
    let prompt = this.homeForm.get('description')?.value;
    let kid = this.homeForm.get('isKidsMovie')?.value;
    let genre = this.homeForm.get('filterGenre')?.value;

    this.movieService.getMovieListFromDescription(prompt, kid, genre).subscribe({
      next: (response) => {
        if (response.body === undefined) {
          return;
        }
        const movieData = JSON.parse(response.body)
        console.log(movieData.movies);

        this.movieList = movieData.movies.map((movie: any) => {
          return {
            budget: movie.budget,
            director: movie.director[0],
            forAdults: movie.forAdults,
            genre: movie.genre[0],
            overview: movie.overview,
            posterPath: movie.posterPath,
            releaseDate: movie.releaseDate,
            releaseYear: movie.releaseDate.substring(0, 4),
            reviews: movie.reviews.map((review: any) => review.content.startsWith("> ") ? review.content.substring(2) : review.content),
            runtime: movie.runtime,
            score: movie.score,
            tagline: movie.tagline,
            title: movie.title,
            voteAverage: movie.voteAverage,
            voteAverageRounded: parseFloat(movie.voteAverage).toFixed(1),
            voteCount: movie.voteCount,
          };
        });
      },
      error: (error) => {
        console.error('Error fetching movie list:', error);
      },
    });
  }

  setReleaseYear() {
    this.movieList.forEach(movie => {
      movie.releaseYear = movie.releaseDate.split('-')[0];
    });
  }

  mockInformation() {
    this.movieList = mockMovieList;
  }

  showMoviePopup(movie: MovieDetails): void {
    this.selectedMovie = movie;
    console.log("Popup triggered!");
  }

  closePopup(): void {
    this.selectedMovie = null;
  }
}
