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
        console.log('Success');
        console.log(response);
        // this.movieList = response;
      },
      error: (error) => {
        console.error('Error fetching movie list:', error);
      },
    });
    this.mockInformation();
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
