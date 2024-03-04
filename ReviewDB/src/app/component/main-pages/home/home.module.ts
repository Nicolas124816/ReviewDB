import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home.component';
import { MovieScoreFieldModule } from '../../../component/field-components/movie-score-field/movie-score-field.module'
import { ForKidsIconModule } from '../../../component/field-components/icons/for-kids-icon/for-kids-icon.module'
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    HomeComponent,
  ],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    MovieScoreFieldModule,
    ForKidsIconModule
  ],
  exports: [
    HomeComponent,
  ],
})
export class HomeModule { }
