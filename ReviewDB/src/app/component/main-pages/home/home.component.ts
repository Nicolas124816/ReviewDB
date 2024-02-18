import { Component, OnInit } from '@angular/core';
import { MovieService } from '../../../service/movie.service';
import { MovieDetails } from '../../../model/movie-details';
import { FormBuilder, FormGroup  } from '@angular/forms';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  movieList: MovieDetails[] = [];
  homeForm: FormGroup | undefined;

  constructor(private movieService: MovieService, private fb: FormBuilder) {}

  ngOnInit() {
    this.initializeForm();
  }

  initializeForm() {
    // this.homeForm = this.fb.group({
    //   description: [''],
    //   isKidMovie: [false]
    // });
  }

  getMovieList() {
    const description = 'mock_description';

    this.movieService.getMovieListFromDescription(description).subscribe({
      next: (response) => {
        this.movieList = response;
      },
      error: (error) => {
        console.error('Error fetching movie list:', error);
      },
    });
  }
}
