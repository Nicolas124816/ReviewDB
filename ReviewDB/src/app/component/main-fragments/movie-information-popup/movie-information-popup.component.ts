import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { MovieDetails } from '../../../model/movie-details';

@Component({
  selector: 'app-movie-information-popup',
  templateUrl: './movie-information-popup.component.html',
  styleUrls: ['./movie-information-popup.component.css']
})
export class MovieInformationPopupComponent implements OnInit {
  @Input() movie?: MovieDetails;
  @Output() close = new EventEmitter<void>();

  allReviews: string[] = [];
  firstMovieReview: string = '';

  ngOnInit(): void {
    console.log('Movie details:', this.movie);
    if (this.movie && this.movie.reviews && this.movie.reviews.length > 0) {
      this.firstMovieReview = this.movie.reviews[0].substring(0, Math.min(750 - this.movie?.overview.length, this.movie.reviews[0].length));
    }
  }

  closePopup(): void {
    this.close.emit();
  }

  setReleaseYear() {
    if (this.movie?.releaseDate) {
      this.movie.releaseYear = this.movie.releaseDate.split('-')[0];
    }
  }

  showAllReviews(): void {
    if (this.movie && this.movie.reviews) {
      this.allReviews = this.movie.reviews;
    }
  }

  showLessReviews(): void {
    this.allReviews = [];
  }
}
