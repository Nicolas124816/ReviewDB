import { Component, OnInit } from '@angular/core';
import { MovieService } from '../../../service/movie.service';
import { MovieDetails } from '../../../model/movie-details';
import { mockMovieList } from '../../../mock/movieListOutput';
import { FormBuilder, FormControl, FormGroup, Validators  } from '@angular/forms';
@Component({
  selector: 'app-example-searches',
  templateUrl: './example-searches.component.html',
  styleUrls: ['./example-searches.component.css']
})

export class ExampleSearchesComponent implements OnInit {
  movieList: MovieDetails[] = [];
  homeForm: FormGroup = new FormGroup({
    description: new FormControl(''),
    isKidMovie: new FormControl(false)
  })

  constructor(private movieService: MovieService, private fb: FormBuilder) {}

  ngOnInit() {
    this.getMovieList();
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
