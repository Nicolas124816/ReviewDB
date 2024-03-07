import { Component, OnInit } from '@angular/core';
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
    isKidsMovie: new FormControl(false)
  });

  constructor(private movieService: MovieService, private fb: FormBuilder) {}

  ngOnInit() {
    this.initializeForm();
  }

  initializeForm() {
    this.homeForm = this.fb.group({
      description: ['', Validators.required],
      isKidsMovie: [false]
    });
  }

  getMovieList() {
    let prompt = this.homeForm.get('description')?.value;
    let adult = this.homeForm.get('isKidsMovie')?.value;

    this.movieService.getMovieListFromDescription(prompt, adult).subscribe({
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
            reviews: movie.reviews.map((review: any) => review.content),
            runtime: movie.runtime,
            score: movie.score,
            tagline: movie.tagline,
            title: movie.title,
            voteAverage: movie.voteAverage,
            voteCount: movie.voteCount,
          };
        });
      },
      error: (error) => {
        console.error('Error fetching movie list:', error);
      },
    });
    // this.mockInformation();
  }

  setReleaseYear() {
    this.movieList.forEach(movie => {
      movie.releaseYear = movie.releaseDate.split('-')[0];
    });
  }

  mockInformation() {
    this.movieList = mockMovieList;
  }
}
