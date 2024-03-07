import { NgModule } from '@angular/core';
import { ExampleSearchesComponent } from './example-searches.component';
import { CommonModule } from '@angular/common';
import { MovieScoreFieldModule } from '../../../component/field-components/movie-score-field/movie-score-field.module'
import { ForKidsIconModule } from '../../../component/field-components/icons/for-kids-icon/for-kids-icon.module'

@NgModule({
  declarations: [
    ExampleSearchesComponent,
  ],
  imports: [
    CommonModule,
    MovieScoreFieldModule,
    ForKidsIconModule
  ],
  exports: [
    ExampleSearchesComponent,
  ],
})
export class ExampleSearchesModule { }
