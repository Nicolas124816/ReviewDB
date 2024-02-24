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
    isKidMovie: new FormControl(false)
  });

  constructor(private movieService: MovieService, private fb: FormBuilder) {}

  ngOnInit() {
    this.initializeForm();
  }

  initializeForm() {
    this.homeForm = this.fb.group({
      description: ['', Validators.required],
      isKidMovie: [false]
    });
  }

  getMovieList() {
    // this.movieService.getMovieListFromDescription(this.homeForm.value).subscribe({
    //   next: (response) => {
    //     this.movieList = response;
    //   },
    //   error: (error) => {
    //     console.error('Error fetching movie list:', error);
    //   },
    // });
    this.mockInformation();
  }

  mockInformation() {
    this.movieList = mockMovieList;
  }
}
