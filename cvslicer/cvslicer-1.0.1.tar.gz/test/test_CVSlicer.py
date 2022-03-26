import cvslicer
import unittest

import numpy as np
import cv2

class TestCVSlicer(unittest.TestCase):
    def setUp(self):
        self.img_loaded  = './img/test_image500x500-inter100px.png'
        return

    def tearDown(self):
        self.img_loaded = None
        return
    
    
    def test_img_parameter_validation(self):
        with self.subTest():
            with self.assertRaises(Exception) as context:
                test_img = cvslicer.CVSlicer(self.img_loaded, 100, 100, 50, 40)
            self.assertTrue("Object's height cannot be equal or taller than 0.5 of cutoff height." == str(context.exception))
        
        with self.subTest():
            with self.assertRaises(Exception) as context:
                test_img = cvslicer.CVSlicer(self.img_loaded, 100, 100, 40, 50)
            self.assertTrue("Object's width cannot be equal or wider than 0.5 of cutoff width." == str(context.exception))
        return    
        
    def test_slice_img_by_borders(self):
        test_img = cvslicer.CVSlicer(self.img_loaded, 100, 100, 40, 40)
        output_images = test_img.slice_img_by_borders()
        
        for output_image in output_images:
            with self.subTest():
                img_test = cv2.imread(output_image[0])
                self.assertTrue(np.mean(img_test[10:-10, 10:-10]) == 255)
        return
    
    def test_slice_img_around_horizontal_borders(self):
        test_img = cvslicer.CVSlicer(self.img_loaded, 100, 100, 40, 40)
        test_img.slice_img_by_borders()
        output_images = test_img.slice_img_around_horizontal_borders()
        
        for output_image in output_images:
            with self.subTest():
                img_test = cv2.imread(output_image[0])
                self.assertTrue(np.mean(img_test[:, img_test.shape[1]//2]) == 0)
        return
        
    def test_slice_img_around_vertical_borders(self):
        test_img = cvslicer.CVSlicer(self.img_loaded, 100, 100, 40, 40)
        test_img.slice_img_by_borders()
        output_images = test_img.slice_img_around_vertical_borders()

        for output_image in output_images:
            with self.subTest():
                img_test = cv2.imread(output_image[0])
                self.assertTrue(np.mean(img_test[img_test.shape[0]//2, :]) == 0)
    
        return
    
    def test_slice_img_around_intersection_of_borders(self):
        test_img = cvslicer.CVSlicer(self.img_loaded, 100, 100, 40, 40)
        test_img.slice_img_by_borders()
        output_images = test_img.slice_img_around_intersection_of_borders()

        for output_image in output_images:
            with self.subTest():
                img_test = cv2.imread(output_image[0])
                self.assertTrue(np.mean(img_test[img_test.shape[0]//2, :]) == 0 and np.mean(img_test[:, img_test.shape[1]//2]) == 0)
                
        return        
        
if __name__ == '__main__':
    unittest.main()            