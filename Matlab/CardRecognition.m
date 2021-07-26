clc;
clear all;

cavallo = imread('cavallospade.bmp');
template2 = imread('tgt2.bmp');
template1 = rgb2gray(cavallo);

vid = videoinput('winvideo', 1, 'YUY2_160x120');
vid.ReturnedColorSpace = 'rgb';
preview(vid);

while(1)
    img1 = getsnapshot(vid);   
    img = rgb2gray(img1);
    
 	drawnow
%	pause
% 	imwrite(img,'tgt1.bmp');
% 	drawnow
% 	break
clc
    A1 = normxcorr2(template1, img);
    A2 = normxcorr2(template2, img);
    
    
    if (max(max(A1)) >= 0.8)
        disp('Two of Clubs')
    end

	if (max(max(A2)) >= 0.8)
        disp('Ten of Spades')
    end

    
%    disp([max(max(A1)), max(max(A2))])

%     [v ind] = max(A);
%     [v ind1] = max(max(A));
%    
%     imshow(img);

    %[m,n]=find(A>=0.75);
    %hold on;
    %plot(n,m,'b.');
    %figure
    %hold off

% 	if (v>=0.75)
%         x = ind1;
%         y = ind(ind1);
%         hold on
%         plot(x-20, y-20,'rx');
%         hold off
% 	end
%     drawnow
end

closepreview(vid);
delete(vid);
clear vid

close(gcf)

%clear