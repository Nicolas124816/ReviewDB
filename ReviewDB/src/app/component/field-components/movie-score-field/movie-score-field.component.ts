import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-movie-score-field',
  templateUrl: './movie-score-field.component.html',
  styleUrls: ['./movie-score-field.component.css']
})
export class MovieScoreFieldComponent {
  @Input() score: number | undefined;
}
